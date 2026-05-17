export default function SearchInput({ value, onChange, placeholder = 'Search...' }) {
  return (
    <input
      className="search-input"
      value={value}
      onChange={(event) => onChange(event.target.value)}
      placeholder={placeholder}
    />
  );
}
