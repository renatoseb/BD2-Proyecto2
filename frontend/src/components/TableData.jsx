import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Box from '@mui/material/Box';


export default class TableData extends React.Component {

  constructor(props) {
    super(props);
    this.data = {
      data_: props.data.data,
      time: props.data.time
    };

    console.log("Las propsss")
    // console.log(props);
  }

  componentDidMount() {
    console.log("table did mount")
  }

  componentDidUpdate() {
    console.log("table did update")
    console.log(this.props)
    let time_ = this.props.data.time;
    let dataa = this.props.data.data;
    this.data = {
      data_: dataa,
      time: time_
    }
  }

  render() {
    return (
      <Box>
        <TableContainer sx={{ height: 440 }}>
          <Table stickyHeader size="small">
            <TableHead>
              <TableRow>
                <TableCell>Title</TableCell>
                {/* <TableCell align="right">Author</TableCell> */}
                {/* <TableCell align="right">Publication</TableCell> */}
                <TableCell align="right">Score</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {this.data.data_.map((row) => (
                <TableRow
                  key={row.title}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {row.title}
                  </TableCell>
                  {/* <TableCell align="right">{row.author}</TableCell> */}
                  {/* <TableCell align="right">{row.publication}</TableCell> */}
                  <TableCell align="right">{row.score}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
        Time: {this.data.time}
      </Box>
    );
  }

}