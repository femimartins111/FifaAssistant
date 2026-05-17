import * as XLSX from 'xlsx';

const DATA_PATHS = {
  players: '/data/players.xlsx',
  playersExtra: '/data/players1.xlsx',
  teams: '/data/allteams.xlsx',
  formations: '/data/formations.xlsx',
  ideas: '/data/ideas.xlsx',
  youthCountries: '/data/yacountry.txt',
};

async function fetchArrayBuffer(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Could not load required file: ${path}`);
  }
  return response.arrayBuffer();
}

async function fetchText(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Could not load required file: ${path}`);
  }
  return response.text();
}

function parseWorkbookRows(arrayBuffer) {
  const workbook = XLSX.read(arrayBuffer, { type: 'array' });
  const firstSheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[firstSheetName];
  return XLSX.utils.sheet_to_json(worksheet, { defval: '' });
}

function cleanTeamName(rawTeam) {
  const teamRaw = String(rawTeam ?? '').trim();
  const teamClean = teamRaw.includes('|') ? teamRaw.split('|')[0].trim() : teamRaw;
  if (!teamClean || ['nan', 'none'].includes(teamClean.toLowerCase())) {
    return 'Free Agents';
  }
  return teamClean;
}

export async function loadPlayers() {
  const [mainBuffer, extraBuffer] = await Promise.all([
    fetchArrayBuffer(DATA_PATHS.players),
    fetchArrayBuffer(DATA_PATHS.playersExtra),
  ]);

  const combinedRows = [...parseWorkbookRows(mainBuffer), ...parseWorkbookRows(extraBuffer)];

  return combinedRows.map((row) => ({
    name: row.Name,
    team: cleanTeamName(row.Team),
    ovr: Number(row.OVR),
    pot: Number(row.POT),
    pos: String(row.POS ?? '').trim(),
    age: Number(row.AGE),
    playerImage: row.Image || '',
    clubImage: row.Image1 || '',
  }));
}

export async function loadTeams() {
  const rows = parseWorkbookRows(await fetchArrayBuffer(DATA_PATHS.teams));
  return rows.map((row) => ({
    name: row.Name,
    ovr: Number(row.OVR),
    att: Number(row.ATT),
    mid: Number(row.MID),
    def: Number(row.DEF),
    avgAge: Number(row.AVAGE),
    image: row.Image || '',
  }));
}

export async function loadFormations() {
  const rows = parseWorkbookRows(await fetchArrayBuffer(DATA_PATHS.formations));
  return rows.map((row) => ({
    formation: String(row.FORMATION ?? '').trim(),
    mode: String(row.MODE ?? '').trim(),
    base: Number(row.BASE),
  }));
}

export async function loadCareerIdeas() {
  const rows = parseWorkbookRows(await fetchArrayBuffer(DATA_PATHS.ideas));
  return rows.map((row) => ({
    category: String(row.Category ?? '').trim(),
    description: String(row['Idea Description'] ?? '').trim(),
  }));
}

export async function loadCountriesByContinent() {
  const text = await fetchText(DATA_PATHS.youthCountries);
  return text
    .split(/\r?\n/)
    .filter(Boolean)
    .reduce((accumulator, line) => {
      const [countryRaw, continentRaw] = line.split(',');
      const country = (countryRaw ?? '').trim();
      const continent = (continentRaw ?? '').trim();
      if (!country || !continent) {
        return accumulator;
      }
      if (!accumulator[continent]) {
        accumulator[continent] = [];
      }
      accumulator[continent].push(country);
      return accumulator;
    }, {});
}

export { DATA_PATHS };
