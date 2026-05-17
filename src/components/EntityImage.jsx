import { safeImage } from '../utils/helpers';

export default function EntityImage({ src, alt, className = 'entity-image', fallback = 'No image' }) {
  const imageSource = safeImage(src);
  if (!imageSource) {
    return <div className={`${className} image-fallback`}>{fallback}</div>;
  }

  return (
    <img
      className={className}
      src={imageSource}
      alt={alt}
      onError={(event) => {
        event.currentTarget.style.display = 'none';
        const fallbackElement = document.createElement('div');
        fallbackElement.className = `${className} image-fallback`;
        fallbackElement.textContent = fallback;
        event.currentTarget.parentNode?.appendChild(fallbackElement);
      }}
    />
  );
}
