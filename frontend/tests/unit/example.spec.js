/*
 * OpenPantheon: the pantheon for Education
 * Copyright (C) 2021 CRI
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
import { shallowMount, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router'
import Buefy from 'buefy' 
import Back from '@/components/Back.vue'

const localVue = createLocalVue()
localVue.use(VueRouter)
localVue.use(Buefy)
const router = new VueRouter()

describe('Back.vue', () => {
  it('Goes back in history', async () => {
    const wrapper = shallowMount(Back, {
    	localVue,
    	router
    })
    router.push('/pantheon/1')
    const currentRoute = router.currentRoute
    await wrapper.find('#back').trigger('click')
    const newRoute = router.currentRoute
    expect(currentRoute).toMatchObject(newRoute)
  })
})
