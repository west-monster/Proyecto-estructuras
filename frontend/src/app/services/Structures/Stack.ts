import { Node } from './Node';
export class Stack {
    private top: Node;
    constructor(){
        this.top = null;

    }
    public push(elm: any): void{
        if (top == null) {
            this.top = new Node(elm);
        }else{
            const aux: Node = new Node(elm);
            aux.next = this.top;
            this.top = aux;
        }
    }
    public pop(): any{
        if (this.empty()) {
            console.error('Stack is empty');
        } else {
            console.log(this.top);
            const aux: Node = this.top;
            this.top = this.top.next;
            return aux.value;
        }
    }
    public empty(): boolean{
        return this.top == null;
    }
}
