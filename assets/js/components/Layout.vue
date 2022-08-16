<script setup>
import { ref } from "vue";
</script>

<template>
    <div class="containa">
        <slot />
    </div>
</template>


<style scoped>
.containa {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}
</style>