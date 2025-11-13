<script setup>
  import Auth from '../Layout/Auth.vue'; 
  import { defineProps } from 'vue';
  
  const props = defineProps({
    usuario :{
        type: Object,
        default:()=>[]
    }
  })
  
</script>
<template>
   <Auth
    titulo = "Home"
    :nome="usuario.nome"
    :cadastro=false
    :info=false
  
    
   >

   </Auth>








</template>
<style></style>