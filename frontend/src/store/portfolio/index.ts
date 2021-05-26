import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { PortfolioState } from './state';

const defaultState: PortfolioState = {
  portfolios: [],
};

export const portfolioModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
