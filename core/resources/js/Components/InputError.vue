<script setup>
defineProps({
  message: String,
  className: {
    type: String,
    default: ''
  }
})
</script>

<template>
  <div v-if="message" class="invalid-feedback d-block" :class="className">
    {{ message }}
  </div>
</template>