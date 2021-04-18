import PropTypes from 'prop-types'
import Button from './Button'

const Header = ({title}) => {
    const onClick = (e) => {
        console.log(e)
    }
    return (
        <header className='header'>
            <h1>{title}</h1>
            
        </header>
    
    )
    }

Header.defaultProps = {
    title: 'Task Tracker'
}
Header.propTypes ={
    title: PropTypes.string,
    color: PropTypes.string,
    onClick: PropTypes.func,
}

const headingStyle = {color:'red', backgroundColor:'black'}
export default Header