# Racial bias review

Focus: Black women. This screen finds candidates; read every flag in context before acting.

## Data

- **FLAG: race coding.** Officers record race by sight; the denominator is Black alone. Alone or in combination is 10% larger. Worst-case ratios: Hispanic 2.9x (from 3.2x), White 2.48x (from 2.74x), Asian 27.9x (from 30.83x). The writeup must state this bound.
- **note: overlapping denominators.** Share of each race-alone group that is also Hispanic: {'Black': 1.6, 'Asian': 0.8}. These residents count in two denominators; small shares are tolerable, large ones need non-Hispanic tables.
- **note: race outside the groups.** 3.0% of victims map to no group. Largest raw codes: `P` 1,550, `U` 430, `I` 140. Check none of them should belong to a group.
- **note: unknown race by sex.** Women 2.6%, men 2.6%.
- **note: small groups.** Under 50,000 residents of the focus sex: Asian. Their rates carry more noise.
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
- **review: Causal claim** (`causes`): "- What, not why: Shows how often assaults are reported, not why. Nothing here measures causes or offenders."  
  The data shows rates, not causes. Keep causal words only in sentences that say a cause is not measured.
- **review: Offender implication** (`offenders`): "- What, not why: Shows how often assaults are reported, not why. Nothing here measures causes or offenders."  
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