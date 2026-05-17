import { useMemo, useState } from 'react';
import CompareTable from '../components/CompareTable';
import PageHeader from '../components/PageHeader';
import PlayerCard from '../components/PlayerCard';
import SearchInput from '../components/SearchInput';
import { useData } from '../context/DataContext';

export default function ComparePage() {
  const { players } = useData();

  const [leftSearchInput, setLeftSearchInput] = useState('');
  const [rightSearchInput, setRightSearchInput] = useState('');

  const [leftSearch, setLeftSearch] = useState('');
  const [rightSearch, setRightSearch] = useState('');

  const leftPlayer = useMemo(() => {
    if (!leftSearch.trim()) return null;

    return players.find((player) =>
      player.name.toLowerCase() === leftSearch.toLowerCase()
    );
  }, [players, leftSearch]);

  const rightPlayer = useMemo(() => {
    if (!rightSearch.trim()) return null;

    return players.find((player) =>
      player.name.toLowerCase() === rightSearch.toLowerCase()
    );
  }, [players, rightSearch]);

  const leftSuggestions = useMemo(() => {
    if (!leftSearchInput.trim()) return [];

    return players
      .filter((player) =>
        player.name.toLowerCase().includes(leftSearchInput.toLowerCase())
      )
      .slice(0, 25);
  }, [players, leftSearchInput]);

  const rightSuggestions = useMemo(() => {
    if (!rightSearchInput.trim()) return [];

    return players
      .filter((player) =>
        player.name.toLowerCase().includes(rightSearchInput.toLowerCase())
      )
      .slice(0, 25);
  }, [players, rightSearchInput]);

  function handleLeftEnter(event) {
    if (event.key === 'Enter') {
      setLeftSearch(leftSearchInput);
    }
  }

  function handleRightEnter(event) {
    if (event.key === 'Enter') {
      setRightSearch(rightSearchInput);
    }
  }

  function selectLeftPlayer(playerName) {
    setLeftSearchInput(playerName);
    setLeftSearch(playerName);
  }

  function selectRightPlayer(playerName) {
    setRightSearchInput(playerName);
    setRightSearch(playerName);
  }

  return (
    <section>
      <PageHeader
        title="Compare Players"
        description="Frontend version of your player comparison helper."
      />

      <div className="toolbar card toolbar-grid-2">
        <div>
          <SearchInput
            value={leftSearchInput}
            onChange={setLeftSearchInput}
            onKeyDown={handleLeftEnter}
            placeholder="Search first player..."
          />

          {leftSuggestions.length > 0 && (
            <div className="search-suggestions">
              {leftSuggestions.map((player) => (
                <button
                  key={`${player.name}-${player.team}-left`}
                  type="button"
                  onClick={() => selectLeftPlayer(player.name)}
                >
                  {player.name} — {player.team}
                </button>
              ))}
            </div>
          )}
        </div>

        <div>
          <SearchInput
            value={rightSearchInput}
            onChange={setRightSearchInput}
            onKeyDown={handleRightEnter}
            placeholder="Search second player..."
          />

          {rightSuggestions.length > 0 && (
            <div className="search-suggestions">
              {rightSuggestions.map((player) => (
                <button
                  key={`${player.name}-${player.team}-right`}
                  type="button"
                  onClick={() => selectRightPlayer(player.name)}
                >
                  {player.name} — {player.team}
                </button>
              ))}
            </div>
          )}
        </div>
      </div>

      <CompareTable leftPlayer={leftPlayer} rightPlayer={rightPlayer} />

      <div className="entity-grid two-columns">
        {leftPlayer ? <PlayerCard player={leftPlayer} /> : null}
        {rightPlayer ? <PlayerCard player={rightPlayer} /> : null}
      </div>
    </section>
  );
}