# Security review

- [ ] No credentials, private keys, populated environment files, or state committed
- [ ] Workload runs as non-root with no privilege escalation
- [ ] Container filesystem and writable paths are intentional
- [ ] Dependencies and images are pinned and scanned
- [ ] Network ingress is restricted to necessary sources and ports
- [ ] Queue dependency is not publicly exposed
- [ ] Cloud workload uses an instance role rather than static credentials
- [ ] CI uses least permissions and short-lived cloud identity
- [ ] Logs avoid secrets and sensitive request content
- [ ] Teardown and credential-revocation procedures are documented
