import Mixpanel from 'mixpanel-browser'
// Full API reference: https://developer.mixpanel.com/docs/javascript-full-api-reference

export const mixpanel = Mixpanel

/**
 * Init Analytics libraries
 */
export const init = () => {
  if (!process.env.VUE_APP_MIXPANEL_PROJECT_TOKEN) {
    console.error('Analytics missing env variable VUE_APP_MIXPANEL_PROJECT_TOKEN')
    return
  }
  // Init Mixpanel
  Mixpanel.init(process.env.VUE_APP_MIXPANEL_PROJECT_TOKEN, {
    // Force route data to EU servers: https://developer.mixpanel.com/docs/javascript#eu-data-residency
    api_host: process.env.VUE_APP_MIXPANEL_API_URL,
    debug: process.env.NODE_ENV === 'development',
  })
  // Useful for testing in dev
  // Mixpanel.reset()
}

/**
 * Wrapper to send event (based on Mixpanel track method), can be adapted later if we use two analytics libraries/tools
 * Ref Mixpanel track method: https://developer.mixpanel.com/docs/javascript-full-api-reference#mixpaneltrack
 * @param eventName
 * @param properties
 * @param options
 * @param callback
 */
export const track = (eventName, properties, options, callback) => {
  try {
    Mixpanel.track(eventName, properties, options, callback)
  } catch (err) {
    // Don't catch error if analytics return an error so it doesn't impact the App
    console.error('Analytics error track', err)
  }
}

/**
 * "Page viewed" analytic event
 * @param page
 * @param additionalProperties
 */
export const pageViewed = (page, additionalProperties) => {
  track('page_viewed', {
    page,
    ...additionalProperties,
  })
  // Increment page views for user authenticated
  mixpanel.people.increment('page_views')
}
