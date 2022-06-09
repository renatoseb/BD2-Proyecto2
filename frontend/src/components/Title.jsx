import Item from '../utils/Item'
import Grid from '@mui/material/Grid'

const Title = (props) => {

    return (
        <Grid container spacing={2} >
            <Grid item xs={12}>
                <Item elevation={4}>
                    {props.title}
                </Item>
            </Grid>
        </Grid>
    )
}

export default Title;