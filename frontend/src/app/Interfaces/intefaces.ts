export interface DataTable {
  id?: number;
  nombre: string;
  precio: number;
  codigo: number;
  cantidad: number;
  fecha: string;
} 
export interface TypeAction{
  type: number;
  past: DataTable[];
  new: DataTable[];
}
export interface History{
  type: number;
  nombre: string;
}