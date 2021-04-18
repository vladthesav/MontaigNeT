import PropTypes from 'prop-types'


const Button = ({color, text, onClick}) =>{
    
    return  <button style = {{backgroundColor:color}} 
    onClick ={onClick} className='btn'>{text}</button>
}

Button.defaultProps = {
    title: 'Add'
}
Button.propTypes ={
    title: PropTypes.string,
}

export default Button