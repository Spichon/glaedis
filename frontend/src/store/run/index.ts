import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import {RunState} from './state';

const defaultState: RunState = {
  runs: [],
};

export const runModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
