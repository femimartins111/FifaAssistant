# FIFA Assistant Frontend

This is a modular React + Vite frontend built from your Python FIFA Assistant logic.

## Install

```bash
npm install
npm run dev
```

## Required hardcoded files

Place these inside `public/data` with the exact filenames:

- `players.xlsx`
- `players1.xlsx`
- `allteams.xlsx`
- `formations.xlsx`
- `ideas.xlsx`
- `yacountry.txt`

## What is implemented

- Player browsing with face image + club badge
- Team browsing with team badge/image
- Player comparison
- Random team generator by difficulty
- Random player generator by filters
- Wonderkid generator
- Youth academy position, country, and speciality generator
- Random budget generator
- Random formation generator
- Career idea generator
- Season stats entry with CSV export and charts

## Notes

- The frontend reads Excel files in the browser using `xlsx`.
- In browsers, SheetJS uses `XLSX.read(...)` with fetched data, not `readFile(...)`.
- If an image URL from your spreadsheets blocks hotlinking, the UI will show a fallback block instead.
