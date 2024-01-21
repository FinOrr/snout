# Snout Ledger

![Snout Ledger Logo](logo.jpeg)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Latest Release](https://img.shields.io/github/release/FinOrr/snout-ledger.svg)](https://github.com/FinOrr/snout-ledger/releases)
[![Build Status](https://img.shields.io/github/workflow/status/FinOrr/snout-ledger/CI?logo=github-actions&label=build)](https://github.com/FinOrr/snout-ledger/actions)
[![Code Quality](https://img.shields.io/codacy/grade/FinOrr/snout-ledger?logo=codacy)](https://www.codacy.com/gh/FinOrr/snout-ledger/dashboard)
[![Code Coverage](https://img.shields.io/codecov/c/github/FinOrr/snout-ledger?logo=codecov)](https://codecov.io/gh/FinOrr/snout-ledger)
[![Dependencies](https://img.shields.io/librariesio/github/FinOrr/snout-ledger?logo=dependabot)](https://libraries.io/github/FinOrr/snout-ledger)
[![Chat on Discord](https://img.shields.io/discord/your-discord-server-id?logo=discord)](https://discord.gg/your-discord-invite)

## Overview

The Snout Ledger is an RFID-tracking, blockchain database: a decentralised system written in Rust that integrates local veterinary RFID data into a national Solana blockchain. 
The goal is to streamline the tracking and identification of pets, preventing euthanasia through timely collaboration with registered veterinarians.

This project was built for the [Encode x Solana Hackathon, 2024](https://www.encode.club/encodesolanahack) and as an excuse for me to learn Rust.

## Features

- **Decentralised Tracking:** Utilise Solana blockchain for secure and decentralised storage of RFID data.
  
- **Efficient Identification:** Streamline the tracking and identification of pets to prevent unnecessary euthanasia.

- **Rust Implementation:** Built in Rust, ensuring efficiency, safety, and performance.

## Getting Started

### Installation

To build the Snout Ledger, follow these steps:

```bash
git clone https://github.com/FinOrr/snout-ledger.git
cd snout-ledger
cargo build --release
