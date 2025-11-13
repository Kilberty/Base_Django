<template>
  <BContainer class="mt-5" fluid="sm">
    <BRow align-h="center">
      <BCol cols="12" md="6" lg="4">
        <BCard>
          <h3 class="text-center mb-4">Login</h3>

          <BForm @submit.prevent="submit">
            <BFormGroup label="Email" label-for="email">
              <BFormInput
                id="email"
                type="email"
                v-model="form.email"
                placeholder="email@email.com"
                required
              ></BFormInput>
            </BFormGroup>

            <BFormGroup label="Senha" label-for="password" class="mt-3">
              <BFormInput
                id="password"
                type="password"
                v-model="form.password"
                placeholder="********"
                required
              ></BFormInput>
            </BFormGroup>

            <div class="d-flex justify-content-end mt-4">
              <BButton type="submit" variant="primary" :disabled="processing">
                Entrar
              </BButton>
            </div>
          </BForm>
        </BCard>
      </BCol>
    </BRow>
  </BContainer>
</template>

<script setup>
import { useForm,router } from "@inertiajs/vue3";
import { BContainer,BRow,BCol,BCard,BForm,BButton,BFormGroup,BFormInput } from "bootstrap-vue-next";
const form = useForm({
  email: "",
  password: "",
});

const submit = () => {
  form.post("/usuarios/login/",{
    onSuccess:()=>{
      router.visit('/home')
    }
  }); // Rota Django que processa o login
};
</script>

<style scoped>

</style>
