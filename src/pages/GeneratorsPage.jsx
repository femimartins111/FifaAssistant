import { useMemo, useState } from 'react';
import PageHeader from '../components/PageHeader';
import PlayerCard from '../components/PlayerCard';
import TeamCard from '../components/TeamCard';
import { useData } from '../context/DataContext';
import {
  formatCurrency,
  getCareerIdea,
  getPositionSpeciality,
  getRandomBudget,
  getRandomFormation,
  getRandomPlayer,
  getRandomTeamByDifficulty,
  getRandomWonderkid,
  getRandomYouthCountry,
  getYouthAcademyPosition,
} from '../utils/random';
import { uniqueValues } from '../utils/helpers';

export default function GeneratorsPage() {
  const { players, teams, formations, careerIdeas, countriesByContinent } = useData();

  const [difficultyResult, setDifficultyResult] = useState(null);
  const [difficultyError, setDifficultyError] = useState('');
  const [randomPlayerResult, setRandomPlayerResult] = useState(null);
  const [playerError, setPlayerError] = useState('');
  const [wonderkidResult, setWonderkidResult] = useState(null);
  const [budgetText, setBudgetText] = useState('');
  const [formationText, setFormationText] = useState('');
  const [careerIdeaText, setCareerIdeaText] = useState('');
  const [youthText, setYouthText] = useState('');

  const [playerForm, setPlayerForm] = useState({
    pos: 'ST',
    ovrMin: 70,
    ovrMax: 80,
    ageMin: 20,
    ageMax: 28,
    potMin: 75,
    potMax: 85,
  });

  const [difficulty, setDifficulty] = useState('Easy');
  const [selectedTeamName, setSelectedTeamName] = useState('');
  const [budgetOverride, setBudgetOverride] = useState('');
  const [defenderCount, setDefenderCount] = useState('');
  const [storyline, setStoryline] = useState('Realistic');
  const [continent, setContinent] = useState('');

  const positions = useMemo(() => uniqueValues(players, (player) => player.pos), [players]);
  const continents = useMemo(() => Object.keys(countriesByContinent).sort(), [countriesByContinent]);
  const selectedTeam = teams.find((team) => team.name === selectedTeamName) || null;

  const runDifficultyGenerator = () => {
    try {
      setDifficultyResult(getRandomTeamByDifficulty(teams, difficulty));
      setDifficultyError('');
    } catch (error) {
      setDifficultyError(error.message);
      setDifficultyResult(null);
    }
  };

  const runRandomPlayer = () => {
    try {
      const result = getRandomPlayer(players, {
        pos: playerForm.pos,
        ovrRange: [Number(playerForm.ovrMin), Number(playerForm.ovrMax)],
        ageRange: [Number(playerForm.ageMin), Number(playerForm.ageMax)],
        potRange: [Number(playerForm.potMin), Number(playerForm.potMax)],
      });
      setRandomPlayerResult(result);
      setPlayerError('');
    } catch (error) {
      setPlayerError(error.message);
      setRandomPlayerResult(null);
    }
  };

  const runWonderkid = () => setWonderkidResult(getRandomWonderkid(players));

  const runBudget = () => {
    if (!selectedTeam) {
      setBudgetText('Select a team first.');
      return;
    }
    const amount = getRandomBudget(selectedTeam, budgetOverride || null);
    setBudgetText(`${selectedTeam.name}: ${formatCurrency(amount)}`);
  };

  const runFormation = () => {
    const result = getRandomFormation(formations, defenderCount ? Number(defenderCount) : null);
    setFormationText(`${result.formation} (${result.mode || 'No mode'})`);
  };

  const runCareerIdea = () => {
    const result = getCareerIdea(careerIdeas, storyline);
    setCareerIdeaText(result.description);
  };

  const runYouthScout = () => {
    if (!continent) {
      setYouthText('Select a continent first.');
      return;
    }
    const position = getYouthAcademyPosition();
    const country = getRandomYouthCountry(countriesByContinent, continent);
    const speciality = getPositionSpeciality(position);
    setYouthText(`${country} | ${position} | ${speciality}`);
  };

  return (
    <section>
      <PageHeader title="Generators" description="Every random feature from your Python helper module, rebuilt for React." />

      <div className="generator-grid">
        <div className="card">
          <h3>Random team by difficulty</h3>
          <select value={difficulty} onChange={(event) => setDifficulty(event.target.value)}>
            <option>Easy</option>
            <option>Medium</option>
            <option>Hard</option>
          </select>
          <button className="primary-btn" onClick={runDifficultyGenerator}>Generate Team</button>
          {difficultyError ? <p className="error-text">{difficultyError}</p> : null}
          {difficultyResult ? <TeamCard team={difficultyResult} /> : null}
        </div>

        <div className="card">
          <h3>Random player by filters</h3>
          <div className="mini-grid">
            <select value={playerForm.pos} onChange={(event) => setPlayerForm({ ...playerForm, pos: event.target.value })}>
              {positions.map((position) => (
                <option key={position}>{position}</option>
              ))}
            </select>
            <input type="number" value={playerForm.ovrMin} onChange={(e) => setPlayerForm({ ...playerForm, ovrMin: e.target.value })} placeholder="OVR min" />
            <input type="number" value={playerForm.ovrMax} onChange={(e) => setPlayerForm({ ...playerForm, ovrMax: e.target.value })} placeholder="OVR max" />
            <input type="number" value={playerForm.ageMin} onChange={(e) => setPlayerForm({ ...playerForm, ageMin: e.target.value })} placeholder="Age min" />
            <input type="number" value={playerForm.ageMax} onChange={(e) => setPlayerForm({ ...playerForm, ageMax: e.target.value })} placeholder="Age max" />
            <input type="number" value={playerForm.potMin} onChange={(e) => setPlayerForm({ ...playerForm, potMin: e.target.value })} placeholder="POT min" />
            <input type="number" value={playerForm.potMax} onChange={(e) => setPlayerForm({ ...playerForm, potMax: e.target.value })} placeholder="POT max" />
          </div>
          <button className="primary-btn" onClick={runRandomPlayer}>Generate Player</button>
          {playerError ? <p className="error-text">{playerError}</p> : null}
          {randomPlayerResult ? <PlayerCard player={randomPlayerResult} /> : null}
        </div>

        <div className="card">
          <h3>Wonderkid generator</h3>
          <button className="primary-btn" onClick={runWonderkid}>Find Wonderkid</button>
          {wonderkidResult ? <PlayerCard player={wonderkidResult} /> : null}
        </div>

        <div className="card">
          <h3>Budget generator</h3>
          <select value={selectedTeamName} onChange={(event) => setSelectedTeamName(event.target.value)}>
            <option value="">Select team</option>
            {teams.map((team) => (
              <option key={team.name}>{team.name}</option>
            ))}
          </select>
          <input value={budgetOverride} onChange={(event) => setBudgetOverride(event.target.value)} placeholder="Optional OVR override" />
          <button className="primary-btn" onClick={runBudget}>Generate Budget</button>
          {budgetText ? <p>{budgetText}</p> : null}
        </div>

        <div className="card">
          <h3>Formation generator</h3>
          <select value={defenderCount} onChange={(event) => setDefenderCount(event.target.value)}>
            <option value="">Any formation</option>
            <option value="3">3 defenders</option>
            <option value="4">4 defenders</option>
            <option value="5">5 defenders</option>
          </select>
          <button className="primary-btn" onClick={runFormation}>Generate Formation</button>
          {formationText ? <p>{formationText}</p> : null}
        </div>

        <div className="card">
          <h3>Career idea</h3>
          <select value={storyline} onChange={(event) => setStoryline(event.target.value)}>
            <option>Realistic</option>
            <option>Challenging</option>
            <option>Fun</option>
            <option>Creative</option>
            <option>Specific</option>
          </select>
          <button className="primary-btn" onClick={runCareerIdea}>Generate Idea</button>
          {careerIdeaText ? <p>{careerIdeaText}</p> : null}
        </div>

        <div className="card">
          <h3>Youth academy scout</h3>
          <select value={continent} onChange={(event) => setContinent(event.target.value)}>
            <option value="">Select continent</option>
            {continents.map((entry) => (
              <option key={entry}>{entry}</option>
            ))}
          </select>
          <button className="primary-btn" onClick={runYouthScout}>Generate Prospect</button>
          {youthText ? <p>{youthText}</p> : null}
        </div>
      </div>
    </section>
  );
}
