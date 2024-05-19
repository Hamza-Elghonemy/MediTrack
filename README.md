# MediTrack
Real-Time Medical Data Monitoring System with Socket Programming and Redis

## Demo Video

![Demo](Icons//mediTrackDemo.gif)


## Objective

This project aims to develop a real-time medical data monitoring system simulating communication between a medical device and a server application. The system features user authentication, data visualization, and real-time updates.

## Technical Skills Utilized

- Python programming
- Redis database interaction
- GUI development with PyQt
- Socket programming (TCP)

## Project Description

### Client (Medical Device Simulator)

The client simulates a medical device that continuously generates data representing vital signs (e.g., heart rate, blood pressure). It includes:
- Random generation of vital sign values within a logical range.
- Serialization of patient ID and vital sign data in JSON format.
- Periodic data transmission to the server via a TCP socket.
- A GUI for user interaction.

### Server

The server:
- Listens for incoming connections from client devices using a TCP socket.
- Connects to a Redis database to store received data as key-value pairs (key: patient ID, value: vital signs).
- Sends updates to the client when new data is needed.

### GUI (Data Visualization and User Authentication)

The GUI:
- Includes a sign-up and login page for nurses and doctors.
- Displays vital signs over time in a clear, user-friendly chart.
- Features a search bar for entering patient IDs.
- Retrieves and visually displays vital sign data from Redis.
- Provides options to filter data by date range or vital sign type.
- Asks the server for any new updates periodically.

## Features

1. **Real-Time Data Monitoring**: Continuously generates and transmits vital sign data.
2. **User Authentication**: Secure sign-up and login for nurses and doctors.
3. **Data Visualization**: Clear and interactive charts for visualizing vital signs.
4. **Data Filtering**: Options to filter data by date range or vital sign type.
5. **Real-Time Updates**: The client periodically checks with the server for new updates.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Server**:
   ```sh
   python server.py
   ```

4. **Run the Client**:
   ```sh
   python client.py
   ```

## Usage

1. **Start the Server**:
   - Ensure the server application is running and listening for client connections.

2. **Register and Login**:
   - Use the GUI to sign up or log in as a nurse or doctor.

3. **Simulate Medical Device**:
   - Start one or more client applications to simulate medical devices sending data.

4. **Visualize Data**:
   - Use the GUI to search for specific patients and visualize their vital signs.
   - Filter data by date range or vital sign type as needed.


## Contributors

- **Contributor 1** - [ahmed taha](https://github.com/tahaaa22)
- **Contributor 2** - [Hamza Elghonemy](https://github.com/Hamza-Elghonemy)


## Contributing

If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.




