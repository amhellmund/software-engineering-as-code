// Copyright (c) 2024 Andi Hellmund. All rights reserved.
//
// This work is licensed under the terms of the BSD-3-Clause license.
// For a copy, see <https://opensource.org/license/bsd-3-clause>.

use std::path::PathBuf;

use anyhow::Result;
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Args {
    #[command(subcommand)]
    cmd: Commands,
}

#[derive(Subcommand, Debug, Clone)]
enum Commands {
    /// Initialize a new SWAC namespace.
    Init {
        /// The root directory to store SWAC artifacts to.
        #[arg(required = true)]
        root_dir: PathBuf,
    },
    /// Check a SWAC namespace for consistency errors.
    Check {
        /// The root directory of the namespace.
        #[arg(required = true)]
        root_dir: PathBuf,
    },
    /// Generate the documentation for a SWAC namespace.
    Generate {
        /// The root directory of the namespace.
        #[arg(required = true)]
        root_dir: PathBuf,
        /// The dynamic data (e.g. test reports) to use for the generation.
        #[arg(long)]
        dynamic_data_dir: Option<PathBuf>,
    },
}

fn main() -> Result<()> {
    let args = Args::parse();
    match args.cmd {
        Commands::Init { root_dir } => swac::init(root_dir),
        Commands::Check { root_dir } => swac::check(root_dir),
        Commands::Generate {
            root_dir,
            dynamic_data_dir,
        } => swac::generate(root_dir, dynamic_data_dir),
    }
}
