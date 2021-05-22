export interface IUserProfile {
    id: string;
}

export interface IBroker {
    id: number;
    name: string;
    logo: string;
}

export interface IAccount {
    id: number;
    name: string;
    broker: IBroker;
    public_status?: boolean;
    private_status?: boolean;
}

export interface IAccountUpdate {
    name: string;
    api_key: string;
    secret_key: string;
}

export interface IAccountCreate {
    broker_id: number;
    name: string;
    api_key: string;
    secret_key: string;
}

export interface IAsset {
    name: string;
    slug: string;
    type: string;
    symbol: string;
    cmc_id: number;
    cmc_rank: number;
    sign: string;
}

export interface IAssetBroker {
    id: number;
    name: string;
    asset: IAsset;
}

export interface IAssetBrokerPair {
    id: number;
    altname: string;
    symbol: string;
    active: boolean;
    base: IAssetBroker;
    quote: IAssetBroker;
}

export interface IPortfolio {
    id: number;
    name: string;
    // percentage: number;
    account: IAccount;
    assets: IAssetBrokerPair[];
    quote_asset_id: number;
    quote_asset: IAssetBroker;
    trade_balance: number;
    // ticker: number;
    // automation_task: IAutomationTask;
}

export interface IPortfolioUpdate {
    name?: string;
    // percentage?: number;
    quote_asset_id?: number;
    asset_broker_pairs: IAssetBrokerPair[];
    // ticker?: number;
}

export interface IPortfolioCreate {
    name: string;
    // percentage: number;
    account_id: number;
    quote_asset_id: number;
    asset_broker_pairs: IAssetBrokerPair[];
    // ticker: number;
}
