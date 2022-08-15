export default function EventsPage({ events }) {
  return (
    <>
      <h1>Hello {events.length}!</h1>
      <ul>
        {events.map((event, index) => <li key={index}>{event}</li>)}
      </ul>
    </>
  );
}