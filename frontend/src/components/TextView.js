import Button from './Button'
import React, { useState } from 'react';

const TextView = ({title}) => {
    const [text, setText] = useState('');

    const onClick = (e) => {
        console.log(text.value);
    }
    return (
        <div>
            <form>
                <label>
                    
                    <input type="text" name="name" 
                     placeholder="The meaning of life is"/>
                </label>
                <input type="submit" value="Submit" />
            </form>
            <textarea></textarea>

        </div>
    
    )
}

export default TextView