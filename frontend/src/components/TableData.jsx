import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Box from '@mui/material/Box';


export default function TableData(props) {
  const data_ = props.data.data;
  const time = props.data.time;
  console.log("DATA!!")
  console.log(data_)
  console.log(time)
  return (
    <Box>
      <TableContainer sx={{ height: 440 }}>
        <Table stickyHeader size="small">
          <TableHead>
            <TableRow>
              <TableCell>Text</TableCell>
              <TableCell align="right">Author</TableCell>
              <TableCell align="right">Title</TableCell>
              <TableCell align="right">Score</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {data_.map((row) => (
              <TableRow
                key={row.title}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.content}
                </TableCell>
                <TableCell align="right"></TableCell>
                <TableCell align="right">{row.title}</TableCell>
                <TableCell align="right">{row.score}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      Time: {time}
    </Box>
  );
}