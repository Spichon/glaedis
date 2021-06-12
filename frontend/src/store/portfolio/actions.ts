import {api} from '../../api';
import {ActionContext} from 'vuex';
import {IPortfolioCreate, IPortfolioUpdate} from '../../interfaces';
import {State} from '../state';
import {PortfolioState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {commitSetPortfolios, commitSetPortfolio, commitRemovePortfolio} from './mutations';
import {commitAddNotification, commitRemoveNotification} from '../main/mutations';

type MainContext = ActionContext<PortfolioState, State>;

export const actions = {
    async actionGetPortfolios(context: MainContext) {
        try {
            const response = await api.getPortfolios();
            if (response) {
                commitSetPortfolios(context, response.data);
            }
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
    async actionUpdatePortfolio(context: MainContext, payload: { id: number, portfolio: IPortfolioUpdate }) {
        try {
            const loadingNotification = {content: 'saving', showProgress: true};
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updatePortfolio(payload.id, payload.portfolio),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetPortfolio(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, {content: 'Portfolio successfully updated', color: 'success'});
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
    async actionCreatePortfolio(context: MainContext, payload: IPortfolioCreate) {
        try {
            const loadingNotification = {content: 'saving', showProgress: true};
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createPortfolio(payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, {content: 'Portfolio successfully created', color: 'success'});
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
    async actionDeletePortfolio(context: MainContext, payload: { id: number }) {
        try {
            const loadingNotification = {content: 'saving', showProgress: true};
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.deletePortfolio(payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemovePortfolio(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, {content: 'Portfolio successfully Deleted', color: 'success'});
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
    // async actionStartAutomation(context: MainContext, payload: { id: number }) {
    //     try {
    //         const startingNotification = {content: 'Starting...', showProgress: true};
    //         commitAddNotification(context, startingNotification);
    //         const response = (await Promise.all([
    //             api.startAutomation(payload.id),
    //             await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
    //         ]))[0];
    //         commitSetPortfolio(context, response.data);
    //         commitRemoveNotification(context, startingNotification);
    //         commitAddNotification(context, {content: 'Automation successfully started', color: 'success'});
    //     } catch (error) {
    //         await dispatchCheckApiError(context, error);
    //     }
    // },
    // async actionPauseAutomation(context: MainContext, payload: { id: number }) {
    //     try {
    //         const PauseNotification = {content: 'Stopping...', showProgress: true};
    //         commitAddNotification(context, PauseNotification);
    //         const response = (await Promise.all([
    //             api.pauseAutomation(payload.id),
    //             await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
    //         ]))[0];
    //         commitSetPortfolio(context, response.data);
    //         commitRemoveNotification(context, PauseNotification);
    //         commitAddNotification(context, {content: 'Automation successfully paused', color: 'success'});
    //     } catch (error) {
    //         await dispatchCheckApiError(context, error);
    //     }
    // },
    // async actionDeleteAutomation(context: MainContext, payload: { id: number }) {
    //     try {
    //         const deleteNotification = {content: 'Deleting...', showProgress: true};
    //         commitAddNotification(context, deleteNotification);
    //         const response = (await Promise.all([
    //             api.deleteAutomation(payload.id),
    //             await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
    //         ]))[0];
    //         commitSetPortfolio(context, response.data);
    //         commitRemoveNotification(context, deleteNotification);
    //         commitAddNotification(context, {content: 'Automation successfully deleted', color: 'success'});
    //     } catch (error) {
    //         await dispatchCheckApiError(context, error);
    //     }
    // },
    async actionGetPortfolioEquityBalance(context: MainContext, payload: { id: number }) {
        try {
            const response = await api.getPortfolioEquityBalance(payload.id);
            if (response) {
                return response.data;
            }
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
    async actionGetPortfolioAssets(context: MainContext, payload: { id: number }) {
        try {
            const response = await api.getPortfolioAssets(payload.id);
            if (response) {
                return response.data;
            }
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
};

const {dispatch} = getStoreAccessors<PortfolioState, State>('');

export const dispatchCreatePortfolio = dispatch(actions.actionCreatePortfolio);
export const dispatchGetPortfolios = dispatch(actions.actionGetPortfolios);
export const dispatchUpdatePortfolio = dispatch(actions.actionUpdatePortfolio);
export const dispatchDeletePortfolio = dispatch(actions.actionDeletePortfolio);
// export const dispatchStartAutomation = dispatch(actions.actionStartAutomation);
// export const dispatchPauseAutomation = dispatch(actions.actionPauseAutomation);
// export const dispatchDeleteAutomation = dispatch(actions.actionDeleteAutomation);
export const dispatchGetPortfolioEquityBalance = dispatch(actions.actionGetPortfolioEquityBalance);
export const dispatchGetPortfolioAssets = dispatch(actions.actionGetPortfolioAssets);
