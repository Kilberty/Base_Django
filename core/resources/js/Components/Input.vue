<script setup>
import { defineProps, defineEmits } from "vue";
import { BCol,BFormGroup,BFormInput} from "bootstrap-vue-next";
defineProps({
  id: String,
  name: String,
  label: String,
  cols: { type: [String, Number], default: "12" }, // Padrão: 12 (100% da largura em mobile)
  sm: [String, Number],   // cols para sm (ex: "6")
  md: [String, Number],   // cols para md (ex: "4")
  lg: [String, Number],   // cols para lg (ex: "3")
  xl: [String, Number],   // cols para xl (ex: "2")
  type: String,
  modelValue: [String, Number],
  placeholder: String,
});

const emit = defineEmits(["update:modelValue"]);
</script>

<template>
      <BCol 
        :cols="cols" 
        :sm="sm"
        :md="md"
        :lg="lg"
        :xl="xl"
        v-bind="$attrs"
      > 
        <BFormGroup :label="label">
          <BFormInput
            :id="id"
            :name="name"
            :value="modelValue"
            :type="type"
            :placeholder="placeholder"
            @input="(event) => emit('update:modelValue', event.target.value)"
          />
        </BFormGroup>
      </BCol>
</template>
<style>
</style>