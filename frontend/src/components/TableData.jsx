import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';


export default function TableData(props) {

	return (
		<TableContainer component={Paper}>
			<Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
				<TableHead>
					<TableRow>
						<TableCell>Text</TableCell>
						<TableCell align="right">Author</TableCell>
						<TableCell align="right">Title</TableCell>
						<TableCell align="right">Score</TableCell>
					</TableRow>
				</TableHead>
				<TableBody>
					{props.data.map((row) => (
						<TableRow
							key={row.title}
							sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
						>
							<TableCell component="th" scope="row">
								{row.text}
							</TableCell>
							<TableCell align="right">{row.author}</TableCell>
							<TableCell align="right">{row.title}</TableCell>
							<TableCell align="right">{row.score}</TableCell>
						</TableRow>
					))}
				</TableBody>
			</Table>
		</TableContainer>
	);
}