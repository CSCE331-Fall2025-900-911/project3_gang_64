import type { Insertable, Selectable, Updateable } from 'kysely';

export enum Role {
	ADMIN = 'manager',
	USER = 'staff',
}

export interface EmployeeTable {
	id: number;
	username: string;
	password: string;
	role: Role;
	archived: boolean;
}

export type Employee = Selectable<EmployeeTable>;
export type NewEmployee = Insertable<EmployeeTable>;
export type EmployeeUpdate = Updateable<EmployeeTable>;
