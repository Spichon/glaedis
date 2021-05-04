import { MainState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    dashboardShowDrawer: (state: MainState) => state.dashboardShowDrawer,
    dashboardMiniDrawer: (state: MainState) => state.dashboardMiniDrawer,
    firstNotification: (state: MainState) => state.notifications.length > 0 && state.notifications[0],
};

const {read} = getStoreAccessors<MainState, State>('');

export const readDashboardMiniDrawer = read(getters.dashboardMiniDrawer);
export const readDashboardShowDrawer = read(getters.dashboardShowDrawer);
export const readFirstNotification = read(getters.firstNotification);
