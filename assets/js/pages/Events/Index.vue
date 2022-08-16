<script setup>
import { ref } from "vue";
const props = defineProps({
    events: Object,
});
</script>


<template>
    <h2>This is the events page</h2>
</template>


<style scoped>
</style>

// import { Link } from '@inertiajs/inertia-react';

// export default function EventsPage({ events }) {
//   return (
//     <>
//       <h1>Hello {events.length}!</h1>
//       <Link href={reverseUrl('contact')}>Contact Us</Link>
//       <ul>
//         {events.map((event, index) => <li key={index}>{event}</li>)}
//       </ul>
//     </>
//   );
// }