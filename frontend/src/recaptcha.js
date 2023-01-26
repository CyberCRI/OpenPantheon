/*
 * OpenPantheon: the pantheon for Education
 * Copyright (C) 2022 Learning Planet Institute
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
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
