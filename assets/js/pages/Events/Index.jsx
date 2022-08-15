import { Link } from '@inertiajs/inertia-react';

export default function EventsPage({ events }) {
  return (
    <>
      <h1>Hello {events.length}!</h1>
      <Link href={reverseUrl('contact')}>Contact Us</Link>
      <ul>
        {events.map((event, index) => <li key={index}>{event}</li>)}
      </ul>
    </>
  );
}