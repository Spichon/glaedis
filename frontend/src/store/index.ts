import Vue from 'vue';
import Vuex, {StoreOptions} from 'vuex';

import {mainModule} from './main';
import {State} from './state';
import {accountModule} from './account';
import {brokerModule} from './broker';
import {portfolioModule} from './portfolio';
import {optimizerModule} from '@/store/optimizer';
import {runModule} from '@/store/run';
import {transactionModule} from '@/store/transaction';

Vue.use(Vuex);

const storeOptions: StoreOptions<State> = {
    modules: {
        main: mainModule,
        account: accountModule,
        broker: brokerModule,
        portofolio: portfolioModule,
        optimizer: optimizerModule,
        run: runModule,
        transaction: transactionModule,
    },
};

export const store = new Vuex.Store<State>(storeOptions);

export default store;
