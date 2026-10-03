# Racial bias review

Focus: Black women. This screen finds candidates; read every flag in context before acting.

## Data

- **note: race coding.** Officers record race by sight; the denominator is Black alone. Alone or in combination is 3% larger. Worst-case ratios: Hispanic 2.34x (from 2.41x), White 3.7x (from 3.8x), Asian 5.74x (from 5.9x). The writeup must state this bound.
- **note: overlapping denominators.** Share of each race-alone group that is also Hispanic: {'Black': 0.4, 'Asian': 0.9}. These residents count in two denominators; small shares are tolerable, large ones need non-Hispanic tables.
- **note: race outside the groups.** 0.4% of victims map to no group. Largest raw codes: `I` 291, `U` 78, `P` 64. Check none of them should belong to a group.
- **note: unknown race by sex.** Women 0.2%, men 0.6%.
- **note: small groups.** Under 50,000 residents of the focus sex: Hispanic, Asian. Their rates carry more noise.
- **note: enforcement and reporting.** Police data reflects where police patrol and who calls them. Heavier policing or more reporting in some neighborhoods raises recorded rates there. The writeup must say the data cannot separate this from real differences.
- **note: controls are not neutral.** Neighborhood, income and housing are shaped by segregation and discrimination. A gap that shrinks after these controls has been located, not explained away; say so.

## Writeup

Files: `index.html`, `README.md`

### index.html
- **review: Causal claim** (`causes`): "Shows how often assaults are reported, not why. Nothing here measures causes or offenders."  
  The data shows rates, not causes. Keep causal words only in sentences that say a cause is not measured.
- **review: Offender implication** (`offenders`): "Shows how often assaults are reported, not why. Nothing here measures causes or offenders."  
  Victim data says nothing about who offended. Remove, or state that offenders are not in the data.

### README.md
- **review: Causal claim** (`causes`): "- **What, not why.** Shows how often assaults are reported, not why. Nothing here measures causes or offenders."  
  The data shows rates, not causes. Keep causal words only in sentences that say a cause is not measured.
- **review: Offender implication** (`offenders`): "- **What, not why.** Shows how often assaults are reported, not why. Nothing here measures causes or offenders."  
  Victim data says nothing about who offended. Remove, or state that offenders are not in the data.
- **review: Offender implication** (`offender`): "- Groups: Hispanic of any race first, otherwise the recorded race. Partner flag from the victim-offender relationship."  
  Victim data says nothing about who offended. Remove, or state that offenders are not in the data.

### Required statements

- present: says it does not explain why
- present: names reporting differences
- present: names the race-coding limit
- present: separates reports from people

## Reviewer questions (answer in prose, not by regex)

- Does any sentence invite the reader to infer who the offenders are?
- Would the framing read the same if the groups were swapped?
- Is the comparison group chosen to make the gap look larger (for example, headlining the most extreme pair)?
- Are structural explanations (segregation, policing intensity, access to services) acknowledged as unmeasured, without being asserted?
- Does the headline survive the race-coding worst case and the least favorable comparison?
- Is the focus group described with agency and dignity, as people harmed, not as a problem?