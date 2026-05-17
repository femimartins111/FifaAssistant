import { createContext, useContext, useEffect, useMemo, useState } from 'react';
import {
  loadCareerIdeas,
  loadCountriesByContinent,
  loadFormations,
  loadPlayers,
  loadTeams,
} from '../data/loaders';

const DataContext = createContext(null);

export function DataProvider({ children }) {
  const [players, setPlayers] = useState([]);
  const [teams, setTeams] = useState([]);
  const [formations, setFormations] = useState([]);
  const [careerIdeas, setCareerIdeas] = useState([]);
  const [countriesByContinent, setCountriesByContinent] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const reloadAllData = async () => {
    setLoading(true);
    setError('');
    try {
      const [loadedPlayers, loadedTeams, loadedFormations, loadedIdeas, loadedCountries] = await Promise.all([
        loadPlayers(),
        loadTeams(),
        loadFormations(),
        loadCareerIdeas(),
        loadCountriesByContinent(),
      ]);

      setPlayers(loadedPlayers);
      setTeams(loadedTeams);
      setFormations(loadedFormations);
      setCareerIdeas(loadedIdeas);
      setCountriesByContinent(loadedCountries);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load data files.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    reloadAllData();
  }, []);

  const value = useMemo(
    () => ({
      players,
      teams,
      formations,
      careerIdeas,
      countriesByContinent,
      loading,
      error,
      reloadAllData,
      metadata: {
        playersCount: players.length,
        teamsCount: teams.length,
        formationsCount: formations.length,
        ideasCount: careerIdeas.length,
        continentsCount: Object.keys(countriesByContinent).length,
      },
    }),
    [players, teams, formations, careerIdeas, countriesByContinent, loading, error]
  );

  return <DataContext.Provider value={value}>{children}</DataContext.Provider>;
}

export function useData() {
  const context = useContext(DataContext);
  if (!context) {
    throw new Error('useData must be used within DataProvider.');
  }
  return context;
}
