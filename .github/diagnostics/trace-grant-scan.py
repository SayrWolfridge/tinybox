from pathlib import Path
p=Path("crates/tinybox-jail/src/grants/mod.rs")
s=p.read_text()
needle='    fn admit(&self, path: &Path, source: &str) -> Option<PathBuf> {\n'
assert s.count(needle)==1
s=s.replace(needle,needle+'        eprintln!("GRANT_SCAN enter source={source} path={path:?}");\n')
needle='        match self.subtree_is_clear(path, &canonical, SUBTREE_MAX_ENTRIES, SUBTREE_MAX_DEPTH) {'
assert s.count(needle)==1
s=s.replace(needle,'        let scan_started = std::time::Instant::now();\n        let scan_result = self.subtree_is_clear(path, &canonical, SUBTREE_MAX_ENTRIES, SUBTREE_MAX_DEPTH);\n        eprintln!("GRANT_SCAN done path={path:?} elapsed={:?} result={scan_result:?}", scan_started.elapsed());\n        match scan_result {')
p.write_text(s)
p=Path("crates/tinybox-module/src/tinybus_module/mod.rs")
s=p.read_text();needle='        let allow_unix_paths = request.allow_unix_paths;'
assert s.count(needle)==1
s=s.replace(needle,needle+'\n        eprintln!("GRANT_SCAN bus handler entered");')
needle='        let grants = grants.map_err(|_| {'
assert s.count(needle)==1
s=s.replace(needle,'        eprintln!("GRANT_SCAN blocking resolver returned");\n'+needle)
p.write_text(s)

p=Path("crates/tinybox-module/tests/rust_homes_manifest_e2e.rs")
s=p.read_text()
needle='    let stderr = String::from_utf8_lossy(&output.stderr);'
assert s.count(needle)==1
s=s.replace(needle,needle+'\n    eprintln!("GRANT_SCAN child mode={mode} stderr:\\n{stderr}");')
p.write_text(s)
