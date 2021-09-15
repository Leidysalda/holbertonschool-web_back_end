<<<<<<< HEAD
export default function guardrail(mathFunction) {
    const queue = [];
    try {
        const value = mathFunction();
        queue.push(value);
    } catch (erro) {
        queue.push(error.toString());
    } finally {
        queue.push('Guardrail was processed')
    }
    return queue;
=======
export default function guardrail(mathFunction) {
    const queue = [];
    try {
        const value = mathFunction();
        queue.push(value);
    } catch (erro) {
        queue.push(error.toString());
    } finally {
        queue.push('Guardrail was processed')
    }
    return queue;
>>>>>>> e9fd4fef0a7a0de51270adc075d0102bf18bd12a
}