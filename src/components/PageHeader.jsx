export default function PageHeader({ title, description, actions }) {
  return (
    <div className="page-header">
      <div>
        <h2>{title}</h2>
        <p className="muted">{description}</p>
      </div>
      {actions ? <div className="header-actions">{actions}</div> : null}
    </div>
  );
}
