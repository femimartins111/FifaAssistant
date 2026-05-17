const YOUTH_POSITIONS = ['GK', 'CB', 'RB', 'LB', 'CDM', 'CM', 'CAM', 'RW', 'LW', 'RF', 'LF', 'ST'];

const SPECIALITIES = {
  GK: ['Goalkeeper', 'Sweeper Keeper'],
  CB: ['Defender', 'Stopper', 'Ball-Playing Defender'],
  LB: ['Fullback', 'Wingback', 'Falseback', 'Attacking Wingback'],
  RB: ['Fullback', 'Wingback', 'Falseback', 'Attacking Wingback'],
  CM: ['Box-to-Box', 'Holding', 'Deep-Lying Playmaker', 'Playmaker', 'Half-Winger'],
  CDM: ['Holding', 'Centre-Half', 'Deep-Lying Playmaker', 'Wide Half'],
  LM: ['Winger', 'Wide Midfielder', 'Wide Playmaker', 'Inside Forward'],
  RM: ['Winger', 'Wide Midfielder', 'Wide Playmaker', 'Inside Forward'],
  CAM: ['Playmaker', 'Shadow Striker', 'Half-Winger', 'Classic 10'],
  LW: ['Winger', 'Inside Forward', 'Wide Playmaker'],
  RW: ['Winger', 'Inside Forward', 'Wide Playmaker'],
  ST: ['Advanced Forward', 'Poacher', 'False 9', 'Target Forward'],
};

const CAREER_CATEGORY_MAP = {
  Realistic: 'Realistic & Grounded',
  Challenging: 'Challenging & Hardcore',
  Fun: 'Fun & Unique Concepts',
  Creative: 'Creative & Story-Driven',
  Specific: 'Specific & Niche',
};

export function getRandomItem(items) {
  if (!items.length) {
    throw new Error('No matching records found.');
  }
  return items[Math.floor(Math.random() * items.length)];
}

export function getTeamsByOvr(teams, ovr) {
  return teams.filter((team) => team.ovr === Number(ovr));
}

export function getRandomTeamByDifficulty(teams, difficulty) {
  const ranges = {
    Easy: [80, 90],
    Medium: [70, 80],
    Hard: [60, 70],
  };

  const selectedRange = ranges[difficulty];
  if (!selectedRange) {
    throw new Error('Invalid difficulty selected.');
  }

  const [min, max] = selectedRange;
  const randomOvr = Math.floor(Math.random() * (max - min + 1)) + min;
  return getRandomItem(getTeamsByOvr(teams, randomOvr));
}

function inRange(value, range) {
  if (Array.isArray(range)) {
    return value >= range[0] && value <= range[1];
  }
  return value === Number(range);
}

export function getRandomPlayer(players, { ovrRange, ageRange, potRange, pos }) {
  const matches = players.filter(
    (player) =>
      inRange(player.ovr, ovrRange) &&
      inRange(player.age, ageRange) &&
      inRange(player.pot, potRange) &&
      player.pos === pos
  );

  return getRandomItem(matches);
}

export function getRandomWonderkid(players) {
  return getRandomItem(
    players.filter((player) => player.age >= 16 && player.age <= 21 && player.pot >= 82 && player.pot <= 90 && player.ovr >= 60 && player.ovr <= 80)
  );
}

export function getYouthAcademyPosition() {
  return getRandomItem(YOUTH_POSITIONS);
}

export function getRandomYouthCountry(countriesByContinent, continent) {
  const countries = countriesByContinent[continent] || [];
  return getRandomItem(countries);
}

export function getPositionSpeciality(pos) {
  return getRandomItem(SPECIALITIES[pos?.toUpperCase()] || ['Unknown Position']);
}

export function getRandomBudget(team, givenOvr) {
  const ovr = givenOvr == null || givenOvr === 'None' ? Number(team.ovr) : Number(givenOvr);
  if (ovr < 60) return randomMillions(1, 5);
  if (ovr < 70) return randomMillions(15, 30);
  if (ovr < 80) return randomMillions(30, 50);
  if (ovr < 90) return randomMillions(50, 150);
  return randomMillions(150, 300);
}

function randomMillions(min, max) {
  return (Math.floor(Math.random() * (max - min + 1)) + min) * 1000000;
}

export function getRandomFormation(formations, defenderCount) {
  const filtered = defenderCount
    ? formations.filter((formation) => Number(formation.base) === Number(defenderCount))
    : formations;
  return getRandomItem(filtered);
}

export function getCareerIdea(careerIdeas, storyline) {
  const category = CAREER_CATEGORY_MAP[storyline];
  if (!category) {
    throw new Error('Invalid storyline selected.');
  }
  return getRandomItem(careerIdeas.filter((idea) => idea.category === category));
}

export function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0,
  }).format(amount);
}
