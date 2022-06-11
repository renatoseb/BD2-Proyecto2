import React, { useState } from "react";
import axios from 'axios';
import Title from "../components/Title"
import TableData from "../components/TableData"
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import PropTypes from 'prop-types';



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
		textAlign: 'left',
	}
}

const boxStyleRow = (height, flex = false, direction = "column") => {
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
		flexDirection: flex ? direction : null
	})
}

function getheader() {
	return {
		headers: {
			'Access-Control-Allow-Origin': '*',
			'Access-Control-Allow-Methods': 'GET',
		}
	}
}

function TabPanel(props) {
	const { children, value, index, ...other } = props;

	return (
		<div
			role="tabpanel"
			hidden={value !== index}
			id={`simple-tabpanel-${index}`}
			aria-labelledby={`simple-tab-${index}`}
			{...other}
		>
			{value === index && (
				<Box sx={{ p: 3 }}>
					<Typography>{children}</Typography>
				</Box>
			)}
		</div>
	);
}

function a11yProps(index) {
	return {
		id: `simple-tab-${index}`,
		'aria-controls': `simple-tabpanel-${index}`,
	};
}

const values = {
	text: "",
	topk: ""
};

const tableDataPython = {
	"data": [],
	"time": "0.000"
};

const tableDataPostgres = {
	"data": [],
	"time": "0.000"
};

const tableDataMongo = {
	"data": [],
	"time": "0.000"
};

const Home = () => {
	const [formValues, setFormValues] = useState(values);
	const [tableValuesPython, setTableValuesPython] = useState(tableDataPython);
	const [tableValuesPostgres, setTableValuesPostgres] = useState(tableDataPostgres);
	const [tableValuesMongo, setTableValuesMongo] = useState(tableDataMongo);
	const [value, setValue] = React.useState(0);


	const handleInputChange = (e) => {
		const { name, value } = e.target;
		setFormValues({
			...formValues,
			[name]: value,
		});
	};

	const resetTable = () => {
		// setTableValuesPython([]);
		// setTableValuesPostgres([]);
	};

	const handleSubmit = (event) => {
		// console.log("holaaa")
		event.preventDefault();
		// resetTable();

		axios.get('http://127.0.0.1:5000/python-req/' + formValues.text + '/' + formValues.topk, getheader())
			.then(res => {
				// const data = res.data;
				// console.log(data);
				setTableValuesPython(tableDataPython);
			}).catch((res) => {
				console.log("Some error ocurred...");
			});

		axios.get('http://127.0.0.1:5000/postgres-req/' + formValues.text + '/' + formValues.topk, getheader())
			.then(res => {
				const data = res.data;
				// console.log(data)
				setTableValuesPostgres(data);
				console.log("Values passed to table");
			}).catch((res) => {
				console.log("Some error ocurred...");
			});

		// axios.get('http://127.0.0.1:5000/mongodb-req/' + formValues.text + '/' + formValues.topk, getheader())
		// 	.then(res => {
		// 		const data = res.data;
		// 		// console.log(data)
		// 		setTableValuesMongo(data);
		// 		console.log("Values passed to table");
		// 	}).catch((res) => {
		// 		console.log("Some error ocurred...");
		// 	});

	};

	const handleChange = (event, newValue) => {
		setValue(newValue);
	};
	TabPanel.propTypes = {
		children: PropTypes.node,
		index: PropTypes.number.isRequired,
		value: PropTypes.number.isRequired,
	};

	return (
		<div>
			<Box sx={{ height: '67px', width: '99%', padding: '10px' }}>
				<Title title="Queries" />
			</Box>
			<Box sx={{ height: '1000px', width: '100%', display: 'flex' }}>

				<Box sx={boxStyleCols("100%", "100%")}>

					<Box sx={boxStyleRow("30%", true)}>
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

					<Box sx={boxStyleRow("65%", true, "row")}>
						<Box sx={boxStyleCols("80%", "48%")}>
							<Title title="Python Top K" />
							<TableData data={tableValuesPython} />
						</Box>
						<Box sx={boxStyleCols("95%", "48%")}>
							<Title title="Postgres/Mongo Top K" />
							<Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
								<Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
									<Tab label="Postgres" {...a11yProps(0)} />
									<Tab label="MongoDB" {...a11yProps(1)} />
								</Tabs>
							</Box>
							<TabPanel value={value} index={0}>
								<TableData data={tableValuesPostgres} />
							</TabPanel>
							<TabPanel value={value} index={1}>
								<TableData data={tableValuesMongo} />
							</TabPanel>

						</Box>
					</Box>

				</Box>
			</Box>
		</div >
	)
}


export default Home;