import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { AccountState } from './state';

const defaultState: AccountState = {
  accounts: [],
};

export const accountModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
