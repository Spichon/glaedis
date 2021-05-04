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
