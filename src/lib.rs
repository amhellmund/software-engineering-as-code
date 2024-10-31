use std::path::PathBuf;

use anyhow::Result;

pub fn init(_root_dir: PathBuf) -> Result<()> {
    Ok(())
}

pub fn check(_root_dir: PathBuf) -> Result<()> {
    Ok(())
}

pub fn generate(_root_dir: PathBuf, _dynamic_data_dir: Option<PathBuf>) -> Result<()> {
    Ok(())
}
