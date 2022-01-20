import { load } from 'recaptcha-v3'

let recaptcha = null

export const init = async () => {
  if (process.env.VUE_APP_RECAPTCHA_SITE_KEY) {
    recaptcha = await load(process.env.VUE_APP_RECAPTCHA_SITE_KEY, {
      renderParameters: process.env.VUE_APP_RECAPTCHA_SITE_KEY,
    })
  }
}

export const getToken = async (action) => {
  // Recaptcha not enabled
  if (recaptcha === null) {
    return null
  }
  try {
    return await recaptcha.execute(action)
  } catch (error) {
    console.error('Failed to get captach token', error)
    throw error
  }
}
