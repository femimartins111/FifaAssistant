export function uniqueValues(items, selector) {
  return [...new Set(items.map(selector).filter(Boolean))].sort((a, b) =>
    String(a).localeCompare(String(b), undefined, { numeric: true, sensitivity: 'base' })
  );
}

export function numberRange(min, max) {
  return Array.from({ length: max - min + 1 }, (_, index) => min + index);
}

export function safeImage(url) {
  if (!url || typeof url !== 'string') {
    return '';
  }
  return url.trim();
}
