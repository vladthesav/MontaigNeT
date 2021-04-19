import Button from './Button'
import React, { useState } from 'react';

const TextView = ({title}) => {
    const [input, setInput] = useState('The meaning of life is');
    const [output, setOutput] = useState('')

    const apiRequest = (e) => {

    }
    const onClick = (e) => {
        console.log(input);

        //api request code here - gotta do error handling too!

        //setOutput(input);
    }
    return (
        <div>
            <form>
                <label>
                    <input type="text" name="input" 
                    onChange={e => setInput(e.target.value)} 
                    placeholder="The meaning of life is"/>
                </label>
            </form>
            <textarea value={output}></textarea>
            <div><Button color='blue' text = 'complete' onClick = {onClick}/></div>
        </div>
        
    
    )
}

export default TextView