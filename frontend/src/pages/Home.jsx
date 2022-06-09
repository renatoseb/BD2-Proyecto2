import React, { useState } from "react";
import Title from "../components/Title"
import TableData from "../components/TableData"
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';


const boxStyleCols = (height, width, inlineBlock = true) => {
	return {
		width: width,
		height: height,
		display: inlineBlock ? 'inline-block' : null,
		p: 1,
		mx: 1,
		bgcolor: (theme) =>
			theme.palette.mode === 'dark' ? '#101010' : 'grey.100',
		color: (theme) =>
			theme.palette.mode === 'dark' ? 'grey.300' : 'grey.800',
		border: '1px solid',
		borderColor: (theme) =>
			theme.palette.mode === 'dark' ? 'grey.800' : 'grey.300',
		borderRadius: 2,
		fontSize: '0.875rem',
		fontWeight: '700',
		textAlign: 'center',
	}
}

const boxStyleRow = (height, flex = false) => {
	return ({
		// width: '25%',
		height: height,
		p: 1,
		bgcolor: (theme) =>
			theme.palette.mode === 'dark' ? '#101010' : 'grey.100',
		color: (theme) =>
			theme.palette.mode === 'dark' ? 'grey.300' : 'grey.800',
		border: '1px solid',
		borderColor: (theme) =>
			theme.palette.mode === 'dark' ? 'grey.800' : 'grey.300',
		borderRadius: 2,
		fontSize: '0.875rem',
		fontWeight: '700',
		textAlign: 'center',
		marginBottom: '10px',
		display: flex ? 'flex' : null,
		flexDirection: flex ? 'column' : null,
	})
}


const values = {
	text: "",
	topk: ""
};

const Home = () => {
	const [formValues, setFormValues] = useState(values);
	const handleInputChange = (e) => {
		const { name, value } = e.target;
		setFormValues({
			...formValues,
			[name]: value,
		});
	};

	const handleSubmit = (event) => {
		event.preventDefault();
		console.log(formValues);
	};

	return (
		<div>
			<Box sx={{ height: '67px', width: '99%', padding: '10px' }}>
				<Title title="Queries" />
			</Box>
			<Box sx={{ height: '850px', width: '100%', display: 'flex' }}>

				<Box sx={boxStyleCols("100%", "100%")}>

					<Box sx={boxStyleRow("34%", true)}>
						<TextField
							id="queryText"
							name="text"
							label="Texto de Consulta"
							multiline
							rows={4}
							value={formValues.text}
							onChange={handleInputChange}
						/>
						<TextField
							id="topK"
							name="topk"
							label="Top K"
							variant="outlined"
							sx={{ marginTop: '10px' }}
							value={formValues.topk}
							onChange={handleInputChange}
						/>
						<Button
							variant="contained"
							sx={{ marginTop: '10px' }}
							onClick={handleSubmit}>Buscar
						</Button>

					</Box>

					<Box sx={boxStyleRow("60%")}>
						<Box sx={boxStyleCols("97%", "48%")}>
							<Title title="Python Top K" />
							<TableData />
						</Box>
						<Box sx={boxStyleCols("97%", "48%")}>
							<Title title="Postgres Top K" />
							<TableData />

						</Box>
					</Box>

				</Box>
			</Box>
		</div >
	)
}


export default Home;