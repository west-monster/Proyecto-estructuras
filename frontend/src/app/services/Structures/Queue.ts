import { Stack } from './Stack';
export class Queue {
    private stack1: Stack;
    private stack2: Stack;

    constructor(){
        this.stack1 = new Stack();
        this.stack2 = new Stack();
    }

    public enqueue(elm: any): void{
        this.stack1.push(elm);
    }

    public dequeue(): any{
        if (!this.empty()) {
            if (this.stack2.empty()) {
                while (!this.stack1.empty()) {
                    this.stack2.push(this.stack1.pop());
                }
            }
            return this.stack2.pop();
        }else{
            console.error('Queue is empty');
        }
    }

    public pop(): any{
        if (!this.empty()) {
            if (this.stack1.empty()) {
                while (!this.stack2.empty()) {
                    this.stack1.push(this.stack2.pop());
                }
            }
            return this.stack1.pop();
        }else{
            console.error('Queue is empty');
        }
    }

    public empty(): boolean{
        return this.stack1.empty() && this.stack2.empty();
    }
}
