<script setup lang="ts">
import { ref } from 'vue'

const code = ref('')
const isValid = ref(false)
const error = ref('')
const loading = ref(false)
const showResults = ref(false)
const lookupData = ref({})

const validateLength = (value: string) => {
  return value.length === 19 || 'Code must be exactly 19 digits.'
}

const validateDigits = (value: string) => {
  return /^\d{19}$/.test(value) || 'Code must contain only digits.'
}

const submitCode = async () => {
  if (!isValid.value) return
  loading.value = true
  error.value = ''
  try {
    // Perform lookup (replace with actual lookup logic)
    // Example:
    // const response = await fetch(`/api/lookup?code=${code.value}`)
    // lookupData.value = await response.json()
    // Simulating lookup
    setTimeout(() => {
      lookupData.value = { code: code.value, detail: 'Sample Detail Information' }
      showResults.value = true
      loading.value = false
    }, 2000)
  } catch (err) {
    error.value = 'Lookup failed. Please try again.'
    loading.value = false
  }
}
</script>

<template>
  <v-app>
    <v-main>
      <v-container class="d-flex justify-center align-center" fluid>
        <v-card class="pa-5" max-width="500">
          <v-form ref="form" v-model="isValid" @submit.prevent="submitCode">
            <v-text-field
              v-model="code"
              label="Enter 19-Digit Code"
              :rules="[validateLength, validateDigits]"
              required
              maxlength="19"
            ></v-text-field>
            <v-btn :disabled="!isValid" color="primary" type="submit"> Search </v-btn>
          </v-form>
          <v-alert v-if="error" type="error" dismissible @dismissed="error = ''" class="mt-4">
            {{ error }}
          </v-alert>
          <v-dialog v-model="showResults" transition="fade-transition" max-width="600px">
            <v-card>
              <v-card-title>Lookup Details</v-card-title>
              <v-card-text>
                <!-- Display lookup details here -->
                {{ lookupData }}
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="showResults = false"> Close </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-progress-circular
            v-if="loading"
            indeterminate
            color="primary"
            class="mt-4"
          ></v-progress-circular>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
