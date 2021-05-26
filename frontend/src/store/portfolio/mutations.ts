import { IPortfolio } from '../../interfaces';
import { PortfolioState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setPortfolios(state: PortfolioState, payload: IPortfolio[]) {
        state.portfolios = payload;
    },
    setPortfolio(state: PortfolioState, payload: IPortfolio) {
        const portfolios = state.portfolios.filter((portfolio: IPortfolio) => portfolio.id !== payload.id);
        portfolios.push(payload);
        state.portfolios = portfolios;
    },
    removePortfolio(state: PortfolioState, payload: IPortfolio) {
        const portfolios = state.portfolios.filter((portfolio: IPortfolio) => portfolio.id !== payload.id);
        state.portfolios = portfolios;
    },
};

const { commit } = getStoreAccessors<PortfolioState, State>('');

export const commitSetPortfolios = commit(mutations.setPortfolios);
export const commitSetPortfolio = commit(mutations.setPortfolio);
export const commitRemovePortfolio = commit(mutations.removePortfolio);

